#coding:gbk
"""
���ߣ��Ŀ���
���ڣ�ʯͷ����������ʷ����
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
        if name == "ʯͷ":
            number = 0
            return number
        if name == "����":
            number = 4
            return number
        if name == "ֽ":
            number = 2
            return number
        if name == "����":
            number = 3
            return number

        if name == "ʷ����":
            number = 1
            return number
"""
����Ϸ�����Ӧ����ͬ������
"""
# ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
# ��Ҫ���Ƿ��ؽ��
# ��дִ�д���,������ɺ�passɾ��
def number_to_name(number):
    if number==0:
       number="ʯͷ"
       return number
    if number==4:
          number ="����"
          return number
    if number == 2:
        number="ֽ"
        return number
    if number == 3:
            number="����"
            return number

    if number==1:
          number="ʷ����"
          return number
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
# ��Ҫ���Ƿ��ؽ��
#��дִ�д���,������ɺ�passɾ��

def rpsls(player_choice):
 """
�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
 """
print("----------------")   # ���"-------- "���зָ�
player_choice= input("����������ѡ��:")
print("���ѡ����ǣ�%s"%player_choice)# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
player_choice_number=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
comp_number=random.randrange(5)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
comp_choice=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
print("����ѡ����ǣ�%s"%comp_choice)# ����Ļ����ʾ�����ѡ����������
if player_choice_number== comp_number: # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    print("���ͼ��������һ����")# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
elif player_choice_number==0 and (comp_number==3 or comp_number==4):
    print("��Ӯ��")
elif player_choice_number == 1 and (comp_number == 4 or comp_number == 0):
        print("��Ӯ��")
elif player_choice_number == 2 and (comp_number == 0 or comp_number == 1):
            print("��Ӯ��")
elif player_choice_number == 3 and (comp_number == 1or comp_number ==4):
                print("��Ӯ��")
elif player_choice_number == 4 and (comp_number ==2 or comp_number ==3):
                    print("��Ӯ��")
else:
        print("������")

#����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
# print("��ӭʹ��RPSLS��Ϸ")
# print("----------------")
# print("����������ѡ��:")

# rpsls(player_choice)


