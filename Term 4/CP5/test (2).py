# � ������ ���������� ��������� ������� ������� ��������� � �������� �����

import math


position = 0
target_position = 5
k = 3
prices = [0, -7, -5, -6, -4, 4, 2, 0]

price_to_come = [-math.inf] * (target_position - position)

for i in range(len(price_to_come)):
    # ���� ������ ��������� ������, ��� ����������� ������
    # �� ��������� �������� ��� ��., ��� ������� � +1, �.�. ����� ���������� �� ���. ���������


	# ����������� ������ �������� ��������� � �� �������, �� ������� ����� ����� ����������
	next_position = position + 1 # ���������� ��������� ��������� �� ��������� �������

	for i in range(position + 1, position + k):
		# ������ ������ ��������� �� ������� ������ ����� ��������, �.�. ��� ���������� �������� < 0
		price_to_come[i] = prices[i]
		break
		#else: # �������� ��� ������� �������� �� ��������� �������
		#	possible_prices = []
		#	possible_prices.append(prices[i]) # ������ ������

		#	# ����� �� ���� �����, ��� ������ ������ ������ ����� ��������?
		#	# ��, ������ ��� ������ ����� ��������, �.�. ���� ���� + ����� �� �������� ����� ����� ����������, � ����� ��� �������������!

		#	#for j in range(1, k)
		#	#possible_prices.append(price_to_come[i - 1])

		print(ways_to_come)
    else:
		break
		


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

