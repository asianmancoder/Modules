import java.util.Scanner;


public class main {
	public static void main(String[] args) {
		String e = encode();
		System.out.println(decode(e));
	}
	
	public static String encode() {
		String output = "";
		String message = "";
		char key;
		Scanner scanner = new Scanner(System.in);
		System.out.println("What will be encoded?");
		message = scanner.nextLine();
		System.out.println("Pick a secret key.");
		key = (char) Integer.parseInt(scanner.nextLine());
		
		for(int i = 0; i < message.length(); i++) {
			output += (char) (message.charAt(i) + key );
		}
		
		return output;
}
	public static String decode(String to_decode) {
		String output = "";
		char key;
		Scanner scanner = new Scanner(System.in);
		System.out.println("This is the string that will be decoded: " + to_decode);
		System.out.println("Pick a secret key.");
		key = (char) Integer.parseInt(scanner.nextLine());
		
		for(int i = 0; i < to_decode.length(); i++) {
			output += (char) (to_decode.charAt(i) - key );
		}
		
		return output;
	}
}
