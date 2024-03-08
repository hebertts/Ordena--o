import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
            yield data, i, j, min_index

        # Swap the found minimum element with the first element
        data[i], data[min_index] = data[min_index], data[i]
        yield data, i, j, min_index

# Create a box visualization
def update_chart(frame, boxes, texts):
    data, i, j, min_index = frame
    for k, text in enumerate(texts):
        text.set_text(str(data[k]))
        if k <= i:
            boxes[k].set_facecolor('lightgreen')  # Already sorted
        else:
            boxes[k].set_facecolor('lightblue')   # Unsorted

    boxes[j].set_facecolor('red')   # Current minimum
    boxes[min_index].set_facecolor('yellow')   # Found minimum

def selection_sort_visualization(data):
    fig, ax = plt.subplots(figsize=(10, 8))  # Adjust the figure size
    num_lines = (len(data) - 1) // 25 + 1  # Calculate the number of lines needed

    boxes = []
    texts = []

    for line in range(num_lines):
        start_index = line * 25
        end_index = min((line + 1) * 25, len(data))
        line_data = data[start_index:end_index]

        for i, number in enumerate(line_data):
            box = plt.Rectangle((i, line), 1, 1, color='lightblue', ec='black')
            ax.add_patch(box)
            boxes.append(box)
            text = ax.text(i + 0.5, line + 0.5, str(number), ha='center', va='center', fontsize=8)  # Adjust font size
            texts.append(text)

    ax.set_xlim(0, 25)
    ax.set_ylim(0, num_lines)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Selection Sort Visualization")

    ani = animation.FuncAnimation(fig, update_chart, frames=selection_sort(data), fargs=(boxes, texts), interval=200, repeat=False)  # Adjust the interval
    plt.show()

if __name__ == "__main__":
    data = list(range(1, 70))  # 100 numbers
    random.shuffle(data)
    selection_sort_visualization(data)
