import java.util.Scanner;

public class Main {
    public static int[] arr;
    public static int N;
    public static int cnt = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new int[N];
        find(0);
        System.out.println(cnt);
    }

    public static void find(int row){
        if(row == N){
            cnt ++;
            return;
        }
        for(int i = 0;i<N;i++){
            arr[row] = i;
            boolean flag = true;
            for(int j = 0;j<row;j++){
                if(arr[row] == arr[j] || row-j == Math.abs(arr[row]-arr[j])){
                    flag = false;
                    break;
                }
            }
            if(flag){
                find(row+1);
            }
        }
    }
}