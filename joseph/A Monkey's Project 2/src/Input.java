 import java.util.Scanner;
public class Input {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner scan = new Scanner(System.in);
        System.out.println("What is your name?"); 
        String name = scan.nextLine();
        System.out.println("What is your favorite number?");
        int num = scan. nextInt();
        System.out.println("name: "+name+"number:"+num);
	}

}
