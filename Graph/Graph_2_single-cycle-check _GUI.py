import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer


class CycleVisualizer(QWidget):
    def __init__(self, array):
        super().__init__()
        
        self.array = array
        self.current_idx = 0
        self.num_element_visited = 0
        self.visited_indices = set()

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
            label.setStyleSheet("background-color: lightgray; padding: 20px;")
            self.grid.addWidget(label, 1, idx)
            self.labels.append(label)
        
        # Add a row for arrows (pointing from current to next index)
        self.arrow_labels = []
        for _ in range(len(self.array) - 1):
            arrow = QLabel("")  # Empty label for arrows between elements
            self.grid.addWidget(arrow, 0, _)
            self.arrow_labels.append(arrow)
        
        # Add a button to start the cycle
        self.start_button = QPushButton("Start Cycle")
        self.start_button.clicked.connect(self.start_cycle)
        self.grid.addWidget(self.start_button, 2, len(self.array)//2)
        
        self.setWindowTitle("Single Cycle Visualization with Arrow Transitions")
        self.show()
    
    def start_cycle(self):
        self.current_idx = 0
        self.num_element_visited = 0
        self.visited_indices = set()
        self.timer.start(1000)  # Start the timer to simulate steps every 1 second
    
    def simulate_step(self):
        # Stop if we visited all elements or revisit the start index prematurely
        if self.num_element_visited == len(self.array) or (self.num_element_visited > 0 and self.current_idx == 0):
            self.timer.stop()
            if self.current_idx == 0 and self.num_element_visited == len(self.array):
                self.labels[self.current_idx].setStyleSheet("background-color: lightgreen; padding: 20px;")
                self.start_button.setText("Cycle Complete")
            else:
                self.labels[self.current_idx].setStyleSheet("background-color: red; padding: 20px;")
                self.start_button.setText("Invalid Cycle")
            return

        # Reset all the arrows and labels to default
        for i in range(len(self.array)):
            self.labels[i].setStyleSheet("background-color: lightgray; padding: 20px;")
        for arrow in self.arrow_labels:
            arrow.setText("")

        # Highlight the current index
        self.labels[self.current_idx].setStyleSheet("background-color: yellow; padding: 20px;")
        
        # Get the next index
        next_idx = self.get_next_idx(self.current_idx)
        
        # Display an arrow between the current and the next index (if they're different)
        if self.current_idx != next_idx:
            direction = "→" if next_idx > self.current_idx else "←"
            self.arrow_labels[min(self.current_idx, next_idx)].setText(direction)
            self.arrow_labels[min(self.current_idx, next_idx)].setStyleSheet("font-size: 20px; text-align: center;")
        
        # Simulate visiting the element
        self.num_element_visited += 1
        self.visited_indices.add(self.current_idx)
        
        # Move to the next index
        self.current_idx = next_idx

    def get_next_idx(self, current_idx):
        jump = self.array[current_idx]
        next_idx = (current_idx + jump) % len(self.array)
        return next_idx if next_idx >= 0 else next_idx + len(self.array)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    array = [2, 3, 1, -4, -4, 2]
    visualizer = CycleVisualizer(array)
    sys.exit(app.exec_())
