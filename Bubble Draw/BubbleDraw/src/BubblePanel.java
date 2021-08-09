import java.util.ArrayList;
import java.awt.event.*;
import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;
import javax.swing.JPanel;


public class BubblePanel extends JPanel {
	Random rand = new Random();
	ArrayList<Bubble> bubbleList; // The ArrayList to which Bubble objects are appended to
	int size = 25; // Size of Bubbles
	
	public BubblePanel() {
		bubbleList = new ArrayList<Bubble>();
		setBackground(Color.BLACK);
		// testBubbles();
		// 'Sets', or activates the Mouse Listeners
		addMouseListener(new BubbleListener());
		addMouseMotionListener(new BubbleListener());
		addMouseWheelListener(new BubbleListener());
	}
	
	public void paintComponent(Graphics canvas) {
		super.paintComponent(canvas);
		
		for(Bubble b: bubbleList) { // Draws all Bubbles in the bubbleList
			b.draw(canvas);
		}
	}
	
	/* This was from when I was testing the app.
	public void testBubbles() {
		for(int i = 0; i < 100; i++) {
			int x = rand.nextInt(600);
			int y = rand.nextInt(400);
			int size = rand.nextInt(50);
			bubbleList.add(new Bubble(x, y, size));
		}
		
		repaint();
	}
	*/
	
	private class BubbleListener extends MouseAdapter {
		public void mousePressed(MouseEvent e) { // Tells what to do when mouse is pressed
			bubbleList.add(new Bubble(e.getX(), e.getY(), size)); // Appends Bubble object to bubbleList
			repaint(); // 'Paints' the Bubbles
		}
		
		public void mouseDragged(MouseEvent e) { // Tells what to do when mouse is dragged
			bubbleList.add(new Bubble(e.getX(), e.getY(), size)); // Appends Bubble object to bubbleList
			repaint(); // 'Paints' the Bubbles
		}
	}
	
	private class Bubble {
		// Attributes for the Bubble object
		private int x;
		private int y;
		private int size;
		private Color color;
		
		public Bubble(int newX, int newY, int newSize) {
			// Regular constructor initialization stuff
			x = newX;
			y = newY;
			size = newSize;
			color = new Color(
					rand.nextInt(256), 
					rand.nextInt(256), 
					rand.nextInt(256)
					);
		}
		
		public void draw(Graphics canvas) { // Draws the Bubble on the screen
			canvas.setColor(color);
			canvas.fillOval(x - size/2, y - size/2, size, size);
		}
	}
}