#include <stdio.h>

int main()
{
  int num,flag=0;
  char str[20];
  scanf("%d", &num);
  scanf("%s", str);
  for(int i=1;i<num;i++)
  {
    if(str[i-1]=='H'&&str[i]=='H')
    { 
      flag=1;
      break;
    }
  }
  if(flag)
    printf("NO\n");
  else
  {
    printf("YES\n");
    for(int i=0;i<num;i++)
      if(str[i]=='.')
        printf("B");
      else
        printf("%c",str[i]);
  }
}

