# ���� ��� ����� ����������!
# � �� ����� �������� ������ ����������, � ��������� ������� �������!

import math

# ways_to_come - ���. �������� ������ � �� ��������, �� ������� ����� ����������
ways_to_come = [1, 1, 1]
price_to_come = [-math.inf] * (len(ways_to_come))

count_of_prev_elements = 0
for i in range(len(ways_to_come)):
	count_of_prev_elements = i - 1

	while True: # �������� ���. �������� ��������� �� ���� ��.
		if i == 0:
			ways_to_come[i] = 1
			price_to_come[i] = 
			break
		else:
			ways_to_come[i] += ways_to_come[count_of_prev_elements]
			count_of_prev_elements -= 1
			if count_of_prev_elements == -1:
				break
print(ways_to_come)

# ����� �������� ������ � �� ��������, �� ������� ������ ����������
ways_to_come.append(0)
ways_to_come.append(0)
ways_to_come.append(0)

k = 3 # ���� ������
position = 3 # �������, �� �������� ����� ���������� ������ ������ ���������

for i in range(position, len(ways_to_come)):
	# ���������� �������������� �������� ��������
	previous_elements = []
	for j in range(k):
		previous_elements.append()

	ways_to_come[i] = max()

