from function_visualizer import FunctionVisualizer

visualizer = FunctionVisualizer()

@visualizer.visualize()
def drip(n: int, string: str):
    if n == 10:
        return
    if n%2 == 1:
        drip(n+1, '한문중은 없나요')
    else:
        drip(n+1, string)

drip(0, '영문중은 있는데 왜')

visualizer.render("algo")