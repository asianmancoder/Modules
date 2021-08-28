
package myFirstProgram;

import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.UIManager;

public class calculator { 
	// Declare and instantiate window components
	JButton button0=new JButton("0");
	JButton button1=new JButton("1");
	JButton button2=new JButton("2");
	JButton button3=new JButton("3");
	JButton button4=new JButton("4");
	JButton button5=new JButton("5");
	JButton button6=new JButton("6");
	JButton button7=new JButton("7");
	JButton button8=new JButton("8");
	JButton button9=new JButton("9");
	JButton buttonPoint = new JButton(".");
	JButton buttonEqual=new JButton("=");
	JButton buttonPlus=new JButton("+");
	JButton buttonMinus=new JButton("-");
	JButton buttonDivide=new JButton("/");
	JButton buttonMultiply=new JButton("*");
	//I added
	JButton delete = new JButton("Del");
	JButton clear = new JButton("Clr");
	JButton sqrt = new JButton("Sqrt");
	JButton mod = new JButton("%");
	Font font = new Font("Arial", Font.PLAIN,30);
	
	JPanel windowContent = new JPanel();
	JTextField displayField = new JTextField(30);
	
	// Constructor creates the components in memory
	// and adds the to the frame using combination of
	// Borderlayout and Gridlayout
	calculator(){
		//windowContent= new JPanel();
		// Set the layout manager for this panel
		BorderLayout bl = new BorderLayout();
		windowContent.setLayout(bl);
		
		// Create the display field and place it in the
		// North area of the window
		//displayField = new JTextField(30);
		windowContent.add("North",displayField);	
		

		// Create the panel with the GridLayout
		// that will contain 12 buttons - 10 numeric ones, and
		// buttons with the point and the equal sign
		JPanel p1 = new JPanel();
		GridLayout gl =new GridLayout(5,3);
		p1.setLayout(gl);
		p1.add(button1);
		p1.add(button2);
		p1.add(button3);
		p1.add(button4);
		p1.add(button5);
		p1.add(button6);
		p1.add(button7);
		p1.add(button8);
		p1.add(button9);
		p1.add(buttonPoint);
		p1.add(button0);
		p1.add(buttonEqual);
		
		//I added
		p1.add(delete);
		p1.add(clear);
		p1.add(sqrt);
		
		// Add the panel p1 to the center area of the window
		windowContent.add("Center",p1);
		// Create the panel with the GridLayout
		// that will contain 4 action buttons -
		// Plus, Minus, Divide and Multiply
		JPanel p2 = new JPanel();
		GridLayout gl2 =new GridLayout(5,1);
		p2.setLayout(gl2);
		p2.add(buttonPlus);
		p2.add(buttonMinus);
		p2.add(buttonMultiply);
		p2.add(buttonDivide);
		
		//I added
		p2.add(mod);
		
//		//I added
//		JPanel p3 = new JPanel();
//		GridLayout gl3 = new GridLayout(1,3);
//		p3.setLayout(gl3);
//		p3.add(delete);
//		p3.add(clear);
//		p3.add(sqrt);
		
		
		
		//I added
		button0.setFont(font);
		button1.setFont(font);
		button2.setFont(font);
		button3.setFont(font);
		button4.setFont(font);
		button5.setFont(font);
		button6.setFont(font);
		button7.setFont(font);
		button8.setFont(font);
		button9.setFont(font);
		buttonPoint.setFont(font);
		buttonPlus.setFont(font);
		buttonMinus.setFont(font);
		buttonDivide.setFont(font);
		buttonMultiply.setFont(font);
		buttonEqual.setFont(font);
		clear.setFont(font);
		delete.setFont(font);
		sqrt.setFont(font);
		mod.setFont(font);
		displayField.setFont(font);
		
		
		//Add the panel p2 to the east area of the window
		windowContent.add("East",p2);
		
		//I added
//		windowContent.add("South",p3);
		
		//Create the frame and add the content pane to it
		
		//I added
		try{
		UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		}catch(Exception e){}
		
		
		JFrame frame = new JFrame("Calculator");
		frame.setContentPane(windowContent);
		
		//I added
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		//set the size of the window to be big enough to
		//accommodate all window controls
		frame.pack();
		
		//I added
		frame.setSize(350,400);
		frame.setResizable(false);
		frame.setLocationRelativeTo(null);
		
		
		//Display the window
		frame.setVisible(true);
		
		
		//Instantiate the event listener and
		//register each button with it
		CalculatorEngine calcEngine = new CalculatorEngine(this);
		button0.addActionListener(calcEngine);
		button1.addActionListener(calcEngine);
		button2.addActionListener(calcEngine);
		button3.addActionListener(calcEngine);
		button4.addActionListener(calcEngine);
		button5.addActionListener(calcEngine);
		button6.addActionListener(calcEngine);
		button7.addActionListener(calcEngine);
		button8.addActionListener(calcEngine);
		button9.addActionListener(calcEngine);
		buttonPoint.addActionListener(calcEngine);
		buttonPlus.addActionListener(calcEngine);
		buttonMinus.addActionListener(calcEngine);
		buttonDivide.addActionListener(calcEngine);
		buttonMultiply.addActionListener(calcEngine);
		buttonEqual.addActionListener(calcEngine);
		
		//I added
		delete.addActionListener(calcEngine);
		sqrt.addActionListener(calcEngine);
		clear.addActionListener(calcEngine);
		mod.addActionListener(calcEngine);
	}
	
public static void main(String[] args) {
	//Instantiate the class Calculator
	new calculator();
	}

}