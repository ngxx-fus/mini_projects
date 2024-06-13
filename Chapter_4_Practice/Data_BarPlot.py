import matplotlib.pyplot as plt

data = {
    "x": [i for i in range(1, 10)],
    "y": [i * i for i in range(1, 10)]
}

plt.bar(
    data["x"], 
    data["y"],   
    align='center'
)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Biểu đồ cột')
plt.grid(True)
plt.show() 
