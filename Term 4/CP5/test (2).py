# � ������ ���������� ��������� ������� ������� ��������� � �������� �����

import math


cur_position = 0
target_position = 5
k = 3
prices = [0, -7, -5, -6, -4, 4, 2, 0]

price_to_come = [-math.inf] * (target_position - cur_position)

next_position = cur_position + 1

# ����������� ������ �������� ��������� � �� �������, �� ������� ����� ����� ����������
for i in range(next_position, cur_position + k + 1): #TODO: ��� ����, ���� k = 1?
	# ������ ������ ��������� �� ������� ������ ����� ��������, �.�. ��� ���������� �������� < 0
	price_to_come[i - 1] = prices[i]

# ����������� ������ �������� ��������� � ��������� �������
for y in range(cur_position + k + 1, target_position + 1):
	# �������� ��� ��������� �������� �� �������
	possible_prices = []
	for j in range(y-k-1, y - 1): # ������������ k ���������� ���
		possible_prices.append(price_to_come[j] + prices[y]) # TODO: �������� � ��������� prices
	price_to_come[y - 1] = max(possible_prices)

print(price_to_come)
		
