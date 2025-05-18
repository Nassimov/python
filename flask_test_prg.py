from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

import sys
import math


class Node:
    """Defines a point."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.r_node: list[int] = []  # Now an instance attribute
        self.d_node: list[int] = []  # Now an instance attribute

    def set_coordination(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def set_r_node(self, x: int, y: int) -> None:
        self.r_node.append(x)
        self.r_node.append(y)

    def set_d_node(self, x: int, y: int) -> None:
        self.d_node.append(x)
        self.d_node.append(y)

    def get_format(self) -> None:
        """Method that prints a greeting message"""
        global width
        global height

        if not (self.x >= 0 and self.x < width):
            raise Exception("0 ≤ x1 < width")
        if not (self.y >= 0 and self.y < height):
            raise Exception("0 ≤ y1 < height")
        if not (self.r_node[0] >= -1 and self.d_node[0] < width):
            raise Exception("-1 ≤ x2, x3 < width")
        if not (self.r_node[1] >= -1 and self.d_node[1] < height):
            raise Exception("-1 ≤ y2, y3 < height")
        print(f"{self.x} {self.y} {self.r_node[0]} {self.r_node[1]} {self.d_node[0]} {self.d_node[1]} ")


class NodeList:

    def __init__(self) -> None:
        self.lines: list[str] = []
        self.nodes: list[list[Node]] = []

    def add_node_in_line(self, node: Node, row: int):
        result: bool = nodeList.is_node_exist(node.x, node.y)
        if result:

            try:
                self.nodes[row].append(node)

            except:
                self.nodes.append([])
                self.nodes[row].append(node)

        return result

    def is_node_exist(self, x: int, y: int):
        return self.lines[y][x] == "0"

    def has_node_r_and_exist(self, x: int, y: int) -> bool:
        global width
        if x < width - 1:
            return self.lines[y][x + 1] == "0"
        return False


nodeList = NodeList()

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

if not (width <= 30 and width > 0):
    raise Exception("0 < width ≤ 30")
if not (height <= 30 and height > 0):
    raise Exception("0 < height ≤ 30")
for row in range(height):
    line = input()  # width characters, each either 0 or .
    nodeList.lines.append(line)
    for col in range(width):

        # setpoint coordinations
        node: Node = Node(col, row)
        if nodeList.add_node_in_line(node, row):

            #  set Right point
            index = col
            while index <= width - 1:
                if nodeList.has_node_r_and_exist(index, row):
                    nodeList.nodes[row][len(nodeList.nodes[row]) - 1].set_r_node(index + 1, row)

                    break
                if width - 1 == index:
                    nodeList.nodes[row][len(nodeList.nodes[row]) - 1].set_r_node(-1, -1)
                index = index + 1
            if height > 1:
                if row > 0:
                    # set upper down nodes

                    row_index = row - 1
                    while row_index >= 0:
                        if nodeList.lines[row_index][col] == "0":
                            nodeList.nodes[row_index][col].set_d_node(col, row)
                            break
                        row_index = row_index - 1

                    nodeList.nodes[row_index][col].get_format()
                    if row == height - 1:  # last row
                        nodeList.nodes[row][col].set_d_node(-1, -1)
                        nodeList.nodes[row][col].get_format()

            else:

                nodeList.nodes[row][len(nodeList.nodes[row]) - 1].set_d_node(-1, -1)
                nodeList.nodes[row][len(nodeList.nodes[row]) - 1].get_format()
        else:

            if height == 1:
                continue
            elif row == height - 1:
                # set upper down nodes

                row_index = row - 1
                while row_index >= 0:
                    if nodeList.lines[row_index][col] == "0":
                        nodeList.nodes[row_index][col].set_d_node(-1, -1)
                        break
                    row_index = row_index - 1
                print(f"{row_index} :: {nodeList.nodes[row_index][col].x},{nodeList.nodes[row_index][col].y}",
                      file=sys.stderr, flush=True)

                nodeList.nodes[row_index][col].get_format()

# To debug: print("Debug messages...", file=sys.stderr, flush=True)