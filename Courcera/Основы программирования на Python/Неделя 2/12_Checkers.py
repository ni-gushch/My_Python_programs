start_v = int(input())
start_h = int(input())
end_v = int(input())
end_h = int(input())
if ((end_h == start_h + 1) and
        ((end_v == start_v + 1) or (end_v == start_v - 1))):
    print("YES")
elif ((end_h == start_h + 2) and ((end_v == start_v) or
      (end_v == start_v + 2) or (end_v == start_v - 2))):
    print("YES")
elif ((end_h == start_h + 3) and ((end_v == start_v + 1) or
      (end_v == start_v - 1) or (end_v == start_v + 3) or
      (end_v == start_v - 3))):
    print("YES")
elif ((end_h == start_h + 4) and ((end_v == start_v) or
      (end_v == start_v + 2) or (end_v == start_v - 2) or
      (end_v == start_v + 4) or (end_v == start_v - 4))):
    print("YES")
elif ((end_h == start_h + 5) and ((end_v == start_v + 1) or
      (end_v == start_v - 1) or (end_v == start_v + 3) or
      (end_v == start_v - 3) or (end_v == start_v + 5) or
      (end_v == start_v - 5))):
    print("YES")
elif ((end_h == start_h + 6) and ((end_v == start_v) or
      (end_v == start_v + 2) or (end_v == start_v - 2) or
      (end_v == start_v + 4) or (end_v == start_v - 4) or
      (end_v == start_v + 6) or (end_v == start_v - 6))):
    print("YES")
elif ((end_h == start_h + 7) and ((end_v == start_v + 1) or
      (end_v == start_v - 1) or (end_v == start_v + 3) or
      (end_v == start_v - 3) or (end_v == start_v + 5) or
      (end_v == start_v - 5) or (end_v == start_v + 7) or
      (end_v == start_v - 7))):
    print("YES")
elif ((end_h == start_h + 8) and ((end_v == start_v) or
      (end_v == start_v + 2) or (end_v == start_v - 2) or
      (end_v == start_v + 4) or (end_v == start_v - 4) or
      (end_v == start_v + 6) or (end_v == start_v - 6) or
      (end_v == start_v + 8) or (end_v == start_v - 8))):
    print("YES")
else:
    print("NO")
