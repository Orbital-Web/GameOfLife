import numpy as np
import cv2


class GameBoard:
    def __init__(self, simsize: int = 128, windowsize: int = 1024, startstate: str = None):
        """
        Creates a simsize by simsize board
        """
        self.simsize: int = simsize       # number of cells
        self.windowsize: int = windowsize   # window size
        
        # initialize board (whether cell is alive or not)
        if startstate == None:  # random init
            self.board = np.random.randint(2, size=(simsize, simsize), dtype=bool)
            
        elif startstate == 0:   # empty init
            self.board = np.zeros((simsize, simsize), dtype=bool)
            
        else:                   # create board from input file
            self.board = np.zeros((simsize, simsize), dtype=bool)
            # read file and convert to array
            with open(startstate, 'r') as f:
                for i, line in enumerate(f):
                    if i > simsize: break
                    cline = line.replace('\n', '')
                    if len(cline) > simsize:
                        raise IndexError(f"simulation size must be at least {len(cline)} to use this startstate")
                    self.board[:len(cline), i] = np.array([True if c == '*' else False for c in list(cline.rstrip())])
        
        # initialize colormap
        x, y = np.meshgrid(np.arange(windowsize), np.arange(windowsize))
        hue = (x + y) / (2 * windowsize - 2)
        hsv = np.dstack((hue * 180/255, np.ones((windowsize, windowsize)), np.ones((windowsize, windowsize))))
        self.colormap = cv2.cvtColor(np.uint8(hsv * 255), cv2.COLOR_HSV2RGB)
    
    
    def update_board(self):
        """
        Updates the board state
        """
        neighbors = self._count_neighbors()
        self.board = (neighbors == 3) | ((neighbors == 2) & self.board)  # True if cell has 3 neighbors or is alive with 2 neighbors
    
    
    def pixelarray(self):
        """
        Converts board to pixels
        """
        cellmask = cv2.resize(np.uint8(self.board), (self.windowsize, self.windowsize), interpolation=cv2.INTER_NEAREST)
        return self.colormap * cellmask[:, :, None]
    
    
    def _count_neighbors(self) -> np.ndarray:
        """
        Returns an array with the number of neighbors for each cell
        """
        padded = np.pad(self.board, 1)      # 0-pad board
        neighbors = np.zeros(padded.shape)  # number of neighbors
        
        # add neighbor counts by shifting the board in all 8 directions
        for horiz in (-1, 0, 1):
            for vert in (-1, 0, 1):
                if not (horiz==0 and vert==0):  # do not include self as neighbor
                    neighbors += np.roll(padded, shift=(horiz, vert), axis=(1, 0))
        
        return neighbors[1:-1, 1:-1]    # "un-pad" the neighbors