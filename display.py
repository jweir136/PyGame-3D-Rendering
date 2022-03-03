##### IMPORT THE REQUIRED MODULES #####
import wireframe
import pygame

class Display(object):
    """
        @summary    The constructor creates a pygame window of a given size and sets
                    system-wide variables

        @param      width   The width of the game window.
        @param      height  The height of the game window.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background = (10, 10, 50)

        self.wireframes = {}
        self.nodeColor = (255, 255, 255)
        self.edgeColor = (200, 200, 200)
        self.nodeRadius = 4

    """
        @summary    Add a new wireframe to the screen, using a given name and JSON
                    wireframe file.

        @param      name        The name to give the wireframe object. This is only for
                                concentation purposes.

        @param      filename    The filename of the JSON wireframe object to import to
                                the screen.  
    """
    def _addWireframe(self, name, filename):
        wireframe_object = wireframe.Wireframe(filename)
        self.wireframes[name] = wireframe_object

    def _rotateAll(self, axis, theta):
        rotateFunction = 'rotate' + axis
        for wireframe_obj in self.wireframes:
            getattr(self.wireframes[wireframe_obj], rotateFunction)(theta)

    def display(self):
        # Fill in the screen background
        self.screen.fill(self.background)

        # draw all the wireframe objects one by one.
        for wireframe_object in self.wireframes.values():
            for node in wireframe_object.nodes:
                pygame.draw.circle(self.screen, self.nodeColor, (int(node[0]), int(node[1])), self.nodeRadius, 0)

            for key in wireframe_object._adj_list.keys():
                start = wireframe_object.nodes[int(key)]
                for idx in wireframe_object._adj_list[key]:
                    end = wireframe_object.nodes[idx]
                    pygame.draw.aaline(self.screen, self.edgeColor, (start[0], start[1]), (end[0], end[1]), 1)


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        for wireframe in self.wireframes:
                            self.wireframes[wireframe].translate("x", -10)
                    elif event.key == pygame.K_RIGHT:
                        for wireframe in self.wireframes:       
                            self.wireframes[wireframe].translate("x", 10)
                    elif event.key == pygame.K_UP:
                        for wireframe in self.wireframes:
                            self.wireframes[wireframe].translate("y", -10)
                    elif event.key == pygame.K_DOWN:
                        for wireframe in self.wireframes:
                            self.wireframes[wireframe].translate("y", 10)
                    elif event.key == pygame.K_MINUS:
                        for wireframe in self.wireframes:
                            self.wireframes[wireframe].scale(0.8)
                    elif event.key == pygame.K_EQUALS:
                        for wireframe in self.wireframes:
                            self.wireframes[wireframe].scale(1.25)
                    elif event.key == pygame.K_q:
                        self._rotateAll('X', 0.1)
                    elif event.key == pygame.K_w:
                        self._rotateAll('X', -0.1)
                    elif event.key == pygame.K_a:
                        self._rotateAll('Y', 0.1)
                    elif event.key == pygame.K_s:
                        self._rotateAll('Y', -0.1)
                    elif event.key == pygame.K_z:
                        pass

            self.screen.fill(self.background)
            self.display()
            pygame.display.flip()