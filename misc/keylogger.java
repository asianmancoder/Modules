import org.jnativehook.GlobalScreen;
import org.jnativehook.NativeHookException;
import org.jnativehook.keyboard.*;
import org.jnativehook.mouse.*;


public class KeyLogger implements NativeKeyListener, NativeMouseListener, NativeMouseInputListener, NativeMouseWheelListener {
	
	public static void main(String[] args) {
		try {
			GlobalScreen.registerNativeHook();
		} catch (NativeHookException e) {
			System.err.println(e.getMessage());
			System.exit(0);
		}
		
		// Adding the NativeKeyListener
		GlobalScreen.addNativeKeyListener(new KeyLogger());
		
		// Adding the NativeMouseListeners
		GlobalScreen.addNativeMouseListener(new KeyLogger());
		GlobalScreen.addNativeMouseMotionListener(new KeyLogger());
		GlobalScreen.addNativeMouseWheelListener(new KeyLogger());
	}
	
	@Override
	public void nativeKeyPressed(NativeKeyEvent arg0) {
		System.out.println("Key Pressed: " + NativeKeyEvent.getKeyText(arg0.getKeyCode()));
	}

	@Override
	public void nativeKeyReleased(NativeKeyEvent arg0) {
		System.out.println("Key Released: " + NativeKeyEvent.getKeyText(arg0.getKeyCode()));
	}

	@Override
	public void nativeKeyTyped(NativeKeyEvent arg0) {
		System.out.println("Key Typed: " + NativeKeyEvent.getKeyText(arg0.getKeyCode()));
	}

	@Override
	public void nativeMouseClicked(NativeMouseEvent arg0) {
		System.out.println("Mouse clicked " + arg0.getClickCount() + " times");
	}

	@Override
	public void nativeMousePressed(NativeMouseEvent arg0) {
		System.out.println("Mouse button pressed: " + arg0.getButton());
	}

	@Override
	public void nativeMouseReleased(NativeMouseEvent arg0) {
		System.out.println("Mouse button released: " + arg0.getButton());
	}
	
	@Override
	public void nativeMouseMoved(NativeMouseEvent arg0) {
		System.out.println("Mouse moved to: (" + arg0.getX() + ", " + arg0.getY() + ")");
	}
	
	@Override
	public void nativeMouseDragged(NativeMouseEvent arg0) {
		System.out.println("Mouse dragged on: (" + arg0.getX() + ", " + arg0.getY() + ")");
	}
	
	@Override
	public void nativeMouseWheelMoved(NativeMouseWheelEvent arg0) {
		System.out.println("Mouse wheel moved. Scroll amount: " + arg0.getScrollAmount() + " Scroll type: " + arg0.getScrollType() + " Scroll direction: " + arg0.getWheelDirection() + " Scroll rotation: " + arg0.getWheelRotation());
	}
}
