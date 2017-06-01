import java.util.*;

public class JavaStdinAndStdoutI {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(scan.hasNextInt()) {
            System.out.println(scan.next());
        }
    }
}
