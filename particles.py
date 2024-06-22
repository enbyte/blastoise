import pygame
import loader
import math
import random

pygame.init()

class ColoredParticle: # representing a type of particle
    def __init__(self, color, size=(3, 3), kill_condition=lambda x, y: False):
        self.color = color
        self.size = size

        self.surface = pygame.Surface(size)
        self.surface.fill(color)

        self.kill_condition = kill_condition

    def draw(self, surface, x, y):
        surface.blit(self.surface, (x, y))



class ImageParticle:
    def __init__(self, image_path, size=None, kill_condition=lambda x, y: False):
        self.image = loader.load_image(image_path)

        if size:
            self.image = pygame.transform.scale(self.image, size)
            self.size = size
        else:
            self.size = self.image.get_size()

        self.kill_condition = kill_condition

    def draw(self, surface, x, y):
        surface.blit(self.image, (x, y))


class ParticleSystem:
    def __init__(self, particle_type, max_particles=None, starting_timestep=0, timestep_delta=1, kill_after=None):
        self.particles = {}
        self.particle_type = particle_type
        self.max_particles = max_particles

        self._timestep = starting_timestep
        self._timestep_delta = timestep_delta

        self._kill_ticks = kill_after


    def _get_oldest(self):
        oldest_timestamp = float('inf')
        oldest_particle = None
        for particle in self.particles:
            for particle_data in self.particles[particle]:
                if particle_data[4] < oldest_timestamp:
                    oldest_timestamp = particle_data[4]
                    oldest_particle = (particle, self.particles[particle].index(particle_data))

        return oldest_particle

    def add_particle(self, particle, x, y, direction, velocity, force=False, verbose=True):
        if self.max_particles and len(self.particles) >= self.max_particles:
            if not force:
                if verbose:
                    print("Particle limit of %d reached, not adding particle" % self.max_particles)
                return
            else:
                if verbose:
                    print("Particle limit of %d reached, adding particle anyway - removing particle" % self.max_particles)
                self.particles[self.oldest[0]].pop(self.oldest[1])

                

        if particle not in self.particles:
            self.particles[particle] = [[x, y, direction, velocity, self._timestep]]
        else:
            self.particles[particle].append([x, y, direction, velocity, self._timestep])

    def update(self, ticks=None, find_oldest=True):
        self._timestep += (self._timestep_delta if not ticks else ticks)
        if find_oldest:
            self.oldest_particle = self._get_oldest() # don't overwirte if find_oldest is not called
    
    def _get_particle_position_and_prune(self, list_data, particle_type):
        starting_x, starting_y, direction, velocity, timestep = list_data

        timesteps_since_particle_created = self._timestep - timestep

        x = int(starting_x + ((math.cos(math.radians(direction)) * velocity) * timesteps_since_particle_created))
        y = int(starting_y + ((math.sin(math.radians(direction)) * velocity) * timesteps_since_particle_created))

        if particle_type.kill_condition(x, y):
            self.particles[self.particle_type].remove(list_data)
            return None, None
        
        return x, y
    
    
    def draw(self, surface, update=True):
        if update:
            self.update()

        for particle_type in self.particles:
            for particle in self.particles[particle_type]:
                x, y = self._get_particle_position_and_prune(particle, particle_type)
                particle_type.draw(surface, x, y) if x and y else None

                if self._kill_ticks and particle[4] + self._kill_ticks <= self._timestep:
                    self.particles[particle_type].remove(particle)


def main():
    red_particle = ColoredParticle((255, 0, 0))

    particle_system = ParticleSystem(red_particle, max_particles=1000, kill_after=100)

    screen = pygame.display.set_mode((500, 500))

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))

        mouse_pos = pygame.mouse.get_pos()
        for i in range(5):
            particle_system.add_particle(red_particle, *mouse_pos, random.randint(0, 360), random.randint(3, 10))

        particle_system.draw(screen)

        pygame.display.flip()

        clock.tick(30)

if __name__ == '__main__':
    main()


        
