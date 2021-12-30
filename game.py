n = int(input("Enter number of rows and column: "))
safe_count = 0;
safe_guessed = 0;


void generategrid(int n, int* arr)
{
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            (*(arr+j+(i*n)))=(rand())%2;
            if ((*(arr+j+(i*n)))==0)
            {
                safe_count+=1;
            }
        }
    }
}