x = object()
y = object()

x_list = [x for i in range(10)]
y_list = [y for j in range(10)]
big_list = list(x_list + y_list)