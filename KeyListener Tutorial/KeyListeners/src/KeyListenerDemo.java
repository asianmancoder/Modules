import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


public class KeyListenerDemo implements KeyListener {
	private JFrame frame;
	private ImageIcon img;
	private JLabel imgLabel;
	
	int x = 0;
	int y = 0;
	
	public KeyListenerDemo() {
		this.frame = new JFrame("Demo");
		this.img = new ImageIcon("letter_a.png");
		this.imgLabel = new JLabel(this.img);
		this.imgLabel.setBounds(this.x, this.y, 300, 300);
		this.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.frame.setSize(840, 840);
		this.frame.setVisible(true);
		this.frame.setLayout(null);
		this.frame.addKeyListener(this);
		this.frame.add(imgLabel);
	}
	
	@Override
	public void keyTyped(KeyEvent e) {
		
	}

	@Override
	public void keyPressed(KeyEvent e) {
		if(e.getKeyCode() == KeyEvent.VK_UP) {
			this.y -= 10;
			imgLabel.setLocation(x, y);
		} else if(e.getKeyCode() == KeyEvent.VK_DOWN) {
			this.y += 10;
			imgLabel.setLocation(x, y);
		} else if(e.getKeyCode() == KeyEvent.VK_RIGHT) {
			this.x += 10;
			imgLabel.setLocation(x, y);
		} else if(e.getKeyCode() == KeyEvent.VK_LEFT) {
			this.x -= 10;
			imgLabel.setLocation(x, y);
		}
	}

	@Override
	public void keyReleased(KeyEvent e) {
		
	}
}
