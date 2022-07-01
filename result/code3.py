def main():
   arg1 = 23
   arg4 = arg1
   arg5 = 18
   arg1 = input("%i")
   arg2 = input("%i")
   arg4 = input("%f")
   arg5 = input("%f")
   arg6 = arg1+arg2*arg4
   arg3 = arg2-(arg1)*arg6
   if(arg6>arg3):
      arg5 = arg2*arg4

   else:
      arg1 = arg5/arg6

   operacao = arg1*arg2/arg3-arg4/arg5*arg6
   return 0


main()