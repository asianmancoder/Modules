import java.util.Scanner;
import java.util.Random;

class guess_game {
    public static void main(String[] args) {
        int guess = 0;
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int randint = random.nextInt(101);

        while(guess != randint) {
            System.out.println("I'm thinking of a number from 0 to 100... what is your guess?");
            guess = scanner.nextInt();

            if(guess > randint && (guess - randint) < 10 || guess - randint == 10) {
                System.out.println("You're very close... your guess is just a little more than the number!");
            }
            else if(guess < randint && (randint - guess) < 10 || randint - guess == 10) {
                System.out.println("You're very close... your guess is just a little less than the number!");
            }
            else if(guess > 100 || guess < 0 && guess != -1) {
                System.out.println("Your guess is off the charts. I don't mean that in a good way.");
            }
            else if(guess == randint) {
                System.out.println("You got it correct!");
                break;
            }
            else if(guess == -1) {
                System.out.println("The number was: " + randint);
                break;
            }else {
                System.out.println("No");
            }
        }
    }
}
