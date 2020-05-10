from Tools import SizeComplexityMeasurer as SizeMeasurer
from Tools import VariableComplexityMeasurer as VariableMeasurer
from Tools import MethodComplexityMeasurer as MethodMeasurer
from Tools import ControlStructureComplexityMeasurer as ControlStructureMeasurer
from Tools import CouplingComplexityMeasurer as CouplingMeasurer
from Tools import InheritanceComplexityMeasurer as InheritanceMeasurer
from prettytable import PrettyTable
# from db import Database as db
#from weightTable import WeightTable as wt
# from pprint import  pprint
code3 = """
import java.awt.event.*;
import java.awt.*;

public class JumpingBox extends java.applet.Applet implements MouseListener, MouseMotionListener, ComponentListener {

	private int mx, my;
	private Dimension size;
	private int onaroll;

	public void init() {
		onaroll = 0;
		setSize(500, 500);
		size = getSize();
		addMouseListener(this);
		addMouseMotionListener(this);
		addComponentListener(this);

	}

	public void update(Graphics g) {

		Dimension newSize = getSize();
		if (size.equals(newSize)) {
			// Erase old box
			g.setColor(getBackground());
			g.drawRect(mx, my, (size.width / 10) - 1, (size.height / 10) - 1);

		} else {

			size = newSize;
			g.clearRect(0, 0, size.width, size.height);
		} // Calculate new position
		mx = (int) (Math.random() * 1000) % (size.width - (size.width / 10));
		my = (int) (Math.random() * 1000) % (size.height - (size.height / 10));

		paint(g);

	}

	public void paint(Graphics g) {

		g.setColor(Color.black);
		g.drawRect(0, 0, size.width - 1, size.height - 1);
		g.drawRect(mx, my, (size.width / 10) - 1, (size.height / 10) - 1);

	}

	public void mouseDragged(MouseEvent e) {
	}

	public void mouseMoved(MouseEvent e) {

		e.consume();

		if ((e.getX() % 3 == 0) && (e.getY() % 3 == 0)) {
			repaint();
		}
	}

	public void mousePressed(MouseEvent e) {

		int x = e.getX();
		int y = e.getY();

		e.consume();
		requestFocus();

		if (mx < x && x < mx + getSize().width / 10 - 1 && my < y && y < my + getSize().height / 10 - 1) {
			// determine if hit

			if (onaroll > 0) {
				// not first hit

				switch (onaroll % 4) {
					// play a sound

					case 0:
						play(getCodeBase(), "sounds/tiptoe.thru.the.tulips.au");
						break;

					case 1:
						play(getCodeBase(), "sounds/danger.au");
						break;

					case 2:
						play(getCodeBase(), "sounds/adapt-or-die.au");
						break;

					case 3:
						play(getCodeBase(), "sounds/cannot.be.completed.au");
						break;

				}
				// switch

				onaroll++;

				if (onaroll > 5) {

					getAppletContext().showStatus("Youre on your way to THE HALL OF FAME:" + onaroll + "Hits!");

				} else {

					getAppletContext().showStatus("YOU'RE ON A ROLL:" + onaroll + "Hits!");

				}

			} else {
				// first hit

				getAppletContext().showStatus("HIT IT AGAIN! AGAIN!");
				play(getCodeBase(), "sounds/that.hurts.au");

				onaroll = 1;

			}

		} else {
			// miss

			getAppletContext().showStatus("You hit nothing at (" + x + ", " + y + "), exactly");
			play(getCodeBase(), "sounds/thin.bell.au");

			onaroll = 0;

		}

		repaint();

	}

	public void mouseReleased(MouseEvent e) {
	}

	public void mouseEntered(MouseEvent e) {

		repaint();

	}

	public void mouseExited(MouseEvent e) {

		repaint();

	}

	public void mouseClicked(MouseEvent e) {
	}

	public void componentHidden(ComponentEvent e) {
	}

	public void componentMoved(ComponentEvent e) {
	}

	public void componentResized(ComponentEvent e) {

		repaint();

	}

	public void componentShown(ComponentEvent e) {

		repaint();

	}

	public void destroy() {

		removeMouseListener(this);
		removeMouseMotionListener(this);

	}

	public String getAppletInfo() {
		return "Title: JumpingBox\n" + "Author: Anonymous";
	}

}

"""

code67 = """ 
    import java.util.Scanner;
 class Years{
   public int getYear(){
	int year;
	String enteredYear;
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the year as a number :");
	enteredYear = sc.next();
	year = Integer.parseInt(enteredYear);
	return year;
   }
 }
//------------------------------------------------------------------------------------------------------------------------------------
 class Months extends Years{
   public int getMonth(){
	int month;
	String enteredMonthNumber;
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter the month number :");
	enteredMonthNumber = sc.next();
	month = Integer.parseInt(enteredMonthNumber);
	return month;
   }
 }
//------------------------------------------------------------------------------------------------------------------------------------
class DaysPerMonth extends Months{ 
 static int numDays = 0;
 public static void main(String[] args) {
   int year;
   Months m = new Months();
   int month = m.getMonth();
   
   if((month < 1) || (month > 12)){ 
     System.out.println("Kindly enter a number between 0 to 13.");
   }
   else {
    switch (month) {
      case 1:
      case 3:
      case 5:
      case 7:
      case 8:
      case 10:
      case 12:
        numDays = 31;
        System.out.println("Month " + month + " consists of " + numDays + " days.");
        break;
      case 4:
      case 6:
      case 9:
      case 11:
       numDays = 30;
       System.out.println("Month " + month + " consists of " + numDays + " days.");
       break;
      case 2:
       year = m.getYear();
       if(year < 1) {
        System.out.println("Kindly enter a valid year.");
       }
       else{
        if(((year % 4 == 0) &&  !(year % 100 == 0)) || (year % 400 == 0)){
         numDays = 29;
		 if(year > 2020){
		  System.out.println("In year " + year + " month " + month + " will consist of " + numDays + " days.");
         }
         else{
          System.out.println("In year " + year + " month " + month + " has consisted of " + numDays + " days.");
         }
        }//if at line 61
        else{
         numDays = 28;
         if (year > 2020){
          System.out.println("In year " + year + " month " + month + " will consist of " + numDays + " days.");
         }
         else{
          System.out.println("In year " + year + " month " + month + " has consisted of " + numDays + " days.");
         }
         break;  
        }//else at line 70
       }//else at line 60
    }//switch at line 37
   }//else at line 36
  }//method
 }//class
"""

code = """ 
    class Item
{
private:
	int itemNo;
	char name[20];
	double price;

public:
	Item(int pItemNo,const char pName[]);
	void setPrice(double pPrice);
	double calcTotal(int qty);
	~Item();
};

Item::Item(int pItemNo,const char pName[])
{
	itemNo = pItemNo;
	strcpy_s(name,pName);
}

void Item::setPrice(double pPrice)
{
	price = pPrice;
}

double Item::calcTotal(int qty)
{
	return price * qty;
}

Item::~Item()
{
	cout << "ITem No "<< itemNo << " deleted"<< endl;
	cout << " Item Name "<< name << " deleted" << endl;
	
}

class SalesPerson
{
private:
	int empNo;
	char name[20];
	double sales;
public:
	SalesPerson(int empno, const char pName[]);
	void calcSales( Item i1, Item i2);
	void printSales();
	~SalesPerson();
};



SalesPerson::SalesPerson(int empno, const char pName[])
{
	empNo = empno;
	strcpy_s(name,pName);
	
}

void SalesPerson::calcSales(Item i1, Item i2)
{
	int qty1 , qty2;

	cout << " Enter Quantity 1: ";
	cin >> qty1;
	cout << " Enter Quantity 2: ";
	cin >> qty2;

	sales = i1.calcTotal(qty1) + i2.calcTotal(qty2);

}

void SalesPerson::printSales()
{
	cout << " EmpNo "  << empNo <<endl;
	cout << " EmpName "  << name  <<endl;
	cout << " Sales " << sales << endl;

}



int main()
{
	SalesPerson s1(1,"UwU");
	Item i1(01, "Cars");
	Item i2(102, "Vans");

	i1.setPrice(10000);
	i2.setPrice(20000);

	
	s1.calcSales(i1,i2);
	s1.printSales();

	system("pause");
    return 0;
}



"""

###################################################################################################

print('\n-> COMPLEXITY DUE TO SIZE\n')

m = SizeMeasurer.SizeComplexityMeasurer(code)

# print(m.code)
lines = m.get_code_lines()
o = m.get_operators()
k = m.get_keywords()
n = m.get_numerical_values()
s = m.get_string_literals()
ide = m.get_identifiers()

t = PrettyTable(['Code', 'Nkw', 'Nid', 'Nop', 'Nnv', 'Nsl', 'Cs'])
t.align['Code'] = 'l'

for i in range(0, len(lines)):
    # total = k[i] + ide[i] + o[i] + n[i] + s[i]
    total = 0
    t.add_row([lines[i], k[i], ide[i], o[i], n[i], s[i], total])

print(t)

##################################################################################################

print('\n-> COMPLEXITY DUE TO Variables\n')

v = VariableMeasurer.VariableComplexityMeasurer(code)

t = PrettyTable(['Code', 'Wvs', 'Npdtv', 'Ncdtv', 'Cv'])
t.align['Code'] = 'l'

for i in range(0, len(lines)):
    t.add_row([lines[i], v.get_variable_scope_weight()[i], v.get_number_of_primitive_data()[i],
               v.get_number_of_composite_data()[i], v.get_variable_complexity()[i]])

print(t)

##################################################################################################

print('\n-> COMPLEXITY DUE TO METHODS\n')

m = MethodMeasurer.MethodComplexityMeasurer(code)

t = PrettyTable(['Code', 'Wmrt', 'Npdtp', 'Ncdtp', 'Cm'])
t.align['Code'] = 'l'

for i in range(0, len(lines)):
    t.add_row([lines[i], m.get_weight_return_type()[i], m.get_number_of_primitive_params()[i],
               m.get_number_of_composite_params()[i], m.get_method_complexity()[i]])

print(t)

##################################################################################################

print('\n-> COMPLEXITY DUE TO Control Structures\n')

c = ControlStructureMeasurer.ControlStructureComplexityMeasurer(code)

t = PrettyTable(['Code', 'Wtcs', 'NC', 'Ccspps', 'Ccs'])
t.align['Code'] = 'l'

for i in range(0, len(lines)):
    t.add_row([lines[i], c.get_weight_due_to_type()[i], c.get_number_of_conditions()[i],
               c.get_weight_due_to_nest()[i], c.get_control_structure_complexity()[i]])

print(t)
#################################################################################################

print('\n-> COMPLEXITY DUE TO Inheritance\n')
ih = InheritanceMeasurer.InheritanceComplexityMeasurer(code)
t = PrettyTable(['Code', 'Ndi', 'Nidi', 'Ti', 'Ci'])
t.align['Code'] = '1'

for i in range(0, len(lines)):
    t.add_row([lines[i], ih.get_ndi()[i], ih.get_nidi()[i], ih.get_ti()[i],
               ih.get_complexity()[i]])

print(t)
##################################################################################################

print('\n-> COMPLEXITY DUE TO Coupling\n')

c = CouplingMeasurer.CouplingComplexityMeasurer(code)

t = PrettyTable(
    ['Code', 'Nr ', 'Nmcms', 'Nmcmd', 'Nmcrms', 'Nmcrmd', 'Nrmcrms', 'Nrmcrmd', 'Nrmcms', 'Nrmcmd', 'Nmrgvs', 'Nmrgvd',
     'Nrmrgvs', 'Nrmrgvd', 'Çcp'])
t.align['Code'] = 'l'

for i in range(0, len(lines)):
    total = c.total[i]
    t.add_row([lines[i], 0, c.rm_to_rm_inside[i], c.rm_to_rm_outside[i], c.rm_to_rcm_inside[i],
               c.rm_to_rcm_outside[i], c.rcm_rcm_inside[i], c.rcm_to_rcm_outside[i], c.rcm_to_rm_inside[i],
               c.rcm_to_rm_outside[i], c.rm_to_global_inside[i], c.rm_to_global_outside[i],
               c.rcm_to_global_inside[i], c.rcm_to_global_outside[i], total])
    print(i)
print(t)

##################################################################################################
# #used to debug database values dont panic
# result = db("SELECT value from method_complexity ORDER BY id")
# pprint(vars(result))
# for row in result.result:
#     print(row[0])
# w = wt()
#
# print(w.get_variable()[0])
# print(w.get_variable()[1])
# print("----------------")
