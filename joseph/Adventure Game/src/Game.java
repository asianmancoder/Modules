import java.util.Scanner;

public class Game {
	
	int choice;
	Scanner scan;

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        new Game();
        
	}
	
	public Game() {
		scan = new Scanner(System.in);
		run();
		
	}

	public void run() {
		System.out.println("You are walking in the woods one day. What do you do?");
		System.out.println("1.Slowly try  to back away.");
		System.out.println("2.Make lots of noise and wave your arms to scare the bear.");
		System.out.println("3.Go to sleep.");
		System.out.println("4.Poke it with a stick.");
		System.out.println("5.Play Dead.");
		System.out.println("6.Fight it with a sword.");
		choice = getInput(6);
		if (choice == 1){
			System.out.println("You escape the bear, but you move so slowly that it is now dark out.");
			System.out.println("1. Try to find your way out of the woods."); 
			System.out.println("2. Try to find shelter for night"); 
			choice = getInput(2);
			if (choice == 1){
				System.out.println("Great job! You found your way back to your house! You won!");
				playAgain(); 
			}
			else if (choice == 2) {
				System.out.println("You search around and find a cave to take shelter in.");
				System.out.println("1. You get sticks and  make a fire. ");
			    System.out.println("2. The Bear finds you in the cave. ");
			    System.out.println("3. You go to sleep. ");
			    choice = getInput(3);
			    if (choice == 1){
			    	System.out.println("You tripped and fell into the fire. You are dead.");
			    	playAgain();
			    }
			}
		}
		else if (choice==2){
			System.out.println("The bear attacks and you die.");
			playAgain();
		}
		else if (choice==3){
			System.out.println("You wake up the next morning, safe.");
			System.out.println("1. You lose hope of finding your way back home and commit suicide by jumping off a nearby cliff that you have found.");
			System.out.println("2. You find your way home.");
			choice = getInput(2);
			if (choice == 1){
				System.out.println("You shattered all your bones and died.");
				playAgain();
			}
			else if (choice == 2){
				System.out.println("You won!");
				playAgain();
			}
			
		}
		else if(choice==4){
			System.out.println("The bear ran off because the stick scared and hurt it. You Win!");
			playAgain();
			
			
		}
		else if (choice==5){
			System.out.println("The bear got bored and went away. You won!");
			playAgain();
			
		}
		else if (choice == 6) {
			System.out.println("The bear grabs the sword and it throws it at you and you die because the sword impaled you.");
			playAgain();
		}
			}
			
		
	
		
	
	private void playAgain() {
		// TODO Auto-generated method stub
		System.out.println("Play Again?"); 
		System.out.println("1. Yes"); 
		System.out.println("2. No"); 
		choice = getInput(2); 
		if (choice == 1){
			new Game(); 
		}
	}

	public int getInput(int numberOfChoices){
		int selectedChoice = -1;
	    while(true){
          
            try{
            	selectedChoice = scan.nextInt();
            	if(selectedChoice > 0 && selectedChoice < numberOfChoices+1){
            		return selectedChoice;
            	
            	}
            	else {
            		System.out.println("Please enter a number between 1 and " + numberOfChoices);
            	}
            }catch (Exception ex){
            	System.out.println("Please enter a number between 1 and " + numberOfChoices);
            	scan = new Scanner(System.in);
            }
        }
	
	
	
	}
}
	
	
