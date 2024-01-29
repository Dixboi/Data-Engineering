
import java.util.ArrayList;  

public class Main
{
	public static void main(String[] args) {
		int total = 2;
		ArrayList<Integer> fib = new ArrayList<Integer>();
		fib.add(1);
		fib.add(2);
		
		int fib_size = fib.size();
		
		while (fib.get(fib_size-1) < 4000000) {
		    fib_size = fib.size();
		    int fib_num = fib.get(fib_size-2 )+ fib.get(fib_size-1);
		    fib.add(fib_num);
		    
		    if (fib_num % 2 == 0) {
		        total += fib_num;
		    }
		}
		
		System.out.println(total);
	}
}
