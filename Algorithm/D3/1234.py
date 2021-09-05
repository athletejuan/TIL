for tc in range(1, 11):
    N,nums = input().split()
    password = []
    for i in range(int(N)):
        if password and nums[i] == password[-1]:
            password.pop()
        else:
            password.append(nums[i])
        # if not password:
        #     password.append(nums[i])
        # else:
        #     if nums[i] == password[-1]:
        #         password.pop()
        #     else:
        #         password.append(nums[i])
    print('#{} {}'.format(tc, ''.join(password)))

# for test_case in range(1, 11):
#     numbers = input().split()[1]
#     num_list = []
#     i = 0
#     for a in numbers:
#         num_list.append(a)
#     while i < len(num_list)-1:
#         if num_list[i] == num_list[i+1]:
#             num_list.pop(i)
#             num_list.pop(i)
#             i = -1
#         i += 1
#     print(f"#{test_case} {''.join(num_list)}")