package javafirst;

import java.util.Scanner;

public class Add {

	public static void main(String[] args) {
		
			System.out.println("Hello World");
			
			Scanner sc = new Scanner(System.in);
			
			System.out.print("Enter Number1: ");
			int num1 = sc.nextInt();
			System.out.print("Enter Number2: ");
			int num2 = sc.nextInt();
			
			System.out.println("Sum:                                              "+(num1+num2));
			sc.close();
			}

}
