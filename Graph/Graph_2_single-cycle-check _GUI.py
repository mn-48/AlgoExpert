import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QPen

class CycleVisualizer(QWidget):
    def __init__(self, array):
        super().__init__()
        
        self.array = array
        self.current_idx = 0
        self.num_element_visited = 0
        self.visited_indices = set()
        self.path = []  # Track the path for line drawing

        # Set up the grid layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.initUI()
        
        # Timer to simulate steps in the cycle
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.simulate_step)
        
    def initUI(self):
        # Set up grid of labels for the array
        self.labels = []
        for idx, value in enumerate(self.array):
            label = QLabel(f"{value}")
            label.setStyleSheet("background-color: lightgray; padding: 20px; border: 1px solid black;")
            label.setAlignment(Qt.AlignCenter)
            self.grid.addWidget(label, 1, idx)
            self.labels.append(label)
        
        # Add a button to start the cycle
        self.start_button = QPushButton("Start Cycle")
        self.start_button.clicked.connect(self.start_cycle)
        self.grid.addWidget(self.start_button, 2, len(self.array)//2)
        
        self.setWindowTitle("Single Cycle Path Visualization")
        self.setGeometry(100, 100, 800, 300)  # Increase height to allow space above the boxes
        self.show()
    
    def start_cycle(self):
        self.current_idx = 0
        self.num_element_visited = 0
        self.visited_indices = set()
        self.path = []  # Clear the path for a new run
        self.update()  # Redraw to clear lines
        self.timer.start(1000)  # Start the timer to simulate steps every 1 second
    
    def simulate_step(self):
        # Stop if we visited all elements or revisit the start index prematurely
        if self.num_element_visited == len(self.array) or (self.num_element_visited > 0 and self.current_idx == 0):
            self.timer.stop()
            if self.current_idx == 0 and self.num_element_visited == len(self.array):
                self.labels[self.current_idx].setStyleSheet("background-color: lightgreen; padding: 20px; border: 1px solid black;")
                self.start_button.setText("Cycle Complete")
            else:
                self.labels[self.current_idx].setStyleSheet("background-color: red; padding: 20px; border: 1px solid black;")
                self.start_button.setText("Invalid Cycle")
            return

        # Highlight the current index
        for i in range(len(self.array)):
            self.labels[i].setStyleSheet("background-color: lightgray; padding: 20px; border: 1px solid black;")
        self.labels[self.current_idx].setStyleSheet("background-color: yellow; padding: 20px; border: 1px solid black;")
        
        # Get the next index and add the current and next index to the path for line drawing
        next_idx = self.get_next_idx(self.current_idx)
        self.path.append((self.current_idx, next_idx))
        self.update()  # Redraw lines
        
        # Simulate visiting the element
        self.num_element_visited += 1
        self.visited_indices.add(self.current_idx)
        
        # Move to the next index
        self.current_idx = next_idx

    def get_next_idx(self, current_idx):
        jump = self.array[current_idx]
        next_idx = (current_idx + jump) % len(self.array)
        return next_idx if next_idx >= 0 else next_idx + len(self.array)

    def paintEvent(self, event):
        # Override paintEvent to draw lines
        if self.path:
            painter = QPainter(self)
            pen = QPen(Qt.black, 3)
            painter.setPen(pen)
            
            # Draw lines for each step in the path
            for current_idx, next_idx in self.path:
                # Get the positions of the current_idx and next_idx but adjust vertically to be above the boxes
                current_pos = self.labels[current_idx].geometry().topLeft()  # Top left corner of the box
                next_pos = self.labels[next_idx].geometry().topLeft()

                # Adjust y-coordinate to be above the box (e.g., 20 pixels above)
                current_pos.setY(current_pos.y() - 20)
                next_pos.setY(next_pos.y() - 20)

                # Draw a line above the boxes
                painter.drawLine(current_pos, next_pos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    array = [2, 3, 1, -4, -4, 2]
    visualizer = CycleVisualizer(array)
    sys.exit(app.exec_())
