package basic;


public class IntegerOverflow {

    static int func3(){
        int a = 10;
        int mod = 1000000007;
        for (int i = 0; i < 10; i++) {
            a = 10 * a % mod;
        }

        return a;
    }
    public static void main(String[] args) {
        char s;

        for(s = 0; s < 128; s++ ){
        }

        int r = 1;
        for (int i = 1; i <= 50; i++) {
            r = r * i % 61;
        }
        System.out.println(r);

        
        System.out.println(func3());

    }    
}
