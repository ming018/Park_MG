import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int total = 0;
        
        String array [] = str.split(" ");

        for (int i = 0; i < array.length; i++){
            if (array[i].length() == 0) { total--; }
            total++;
        }
        System.out.println(total);
    }
}