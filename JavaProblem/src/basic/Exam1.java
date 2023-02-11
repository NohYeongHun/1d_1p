package basic;

import java.util.Arrays;

public class Exam1 {

    static int func(int n){
        // O(N)
        int ret = 0;
        for (int i = 1; i <= n; i++) {
            if(i % 3 == 0 || i % 5 == 0){
                ret += i;
            }
        }
        return ret;
    }

    static int func2(int[] arr, int n){
        if(n < 2){
            return 0;
        }

        Arrays.sort(arr);
        for (int cur = 0; cur < n; cur++) {
            
            int left = cur + 1, right = n;
            
            while(left < right){
                int mid = (left + right) / 2;
                int val = arr[mid] + arr[cur];

                if (val < 100){
                    left = mid + 1;
                } 
                if (val == 100){
                    return 1;
                }
                if (val > 100){
                    right = mid;
                }
            }
        }
        
        return 0;
    }

    static int func3(int n){

        for (int i = 1; i * i <= n; i++) {
            if (i * i == n){
                return 1;
            }
        }

        return 0;
    }

    static int func4(int n){
        int ret = 1;

        while(ret * 2 <= n){
            ret *= 2;
        }

        return ret;
    }
    public static void main(String[] args) {
        func(16);
        System.out.println(func2(new int[]{1, 52, 48}, 3));
        System.out.println(func2(new int[]{50, 42}, 2));
        System.out.println(func2(new int[]{4, 13, 63, 87}, 4));
        System.out.println(func3(756580036));
        System.out.println(func4(5));
        System.out.println(func4(97615282));
        
    }
    
}
