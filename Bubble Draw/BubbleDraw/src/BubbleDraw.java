import javax.swing.JFrame;


public class BubbleDraw extends JFrame {
 public static void main(String[] args) {
 JFrame frame = new JFrame("BubbleDraw App"); // Creates a new JFrame instance and sets the title for the window
 frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Basically just tells the application to stop running when the user closes the window
 frame.getContentPane().add(new BubblePanel()); // Main content is set to the BubblePanel class in BubblePanel.java
 frame.setSize(new java.awt.Dimension(600,400)); // Sets window dimensions
 frame.setVisible(true); // Sets the JFrame's visibility status to true
 }
}