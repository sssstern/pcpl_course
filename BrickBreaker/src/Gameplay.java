import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.Timer; 
import javax.swing.JPanel;

public class Gameplay extends JPanel implements KeyListener, ActionListener {   //implements — это ключевое слово, которое указывает, что класс должен предоставить 
																				//определённое поведение, описанное в интерфейсе, и предоставить реализацию для всех методов, объявленных в этом интерфейсе.
																				//extends - значит, что класс будет рассширять контейнер	
	private boolean play = false;         //переменная опредляющая состояние игрового процесса
	private int score =0; 					//переменная хранит количество очков
	private int totalbricks = 21;           //количество дощечек
	private Timer time;                     //таймер
	private int delay = 5;                  //
	private int player1= 310;				//начальное положение платформы
	private int ballposx = 120;				//начальное положение шара
	private int ballposy = 350;
	private int ballxdir = -1;              //начальные направления
	private int ballydir = -2;
	
	private mapbrick map;                    //создаем перемнную типа мапбрик    
	
	public Gameplay() {
		map = new mapbrick (3,7);       //создаем пространство дощечек 
		addKeyListener(this);                    //контруктор для клавиш
		setFocusable(true);             //возмоность получения отклика от акивных клавиш
		time = new Timer(delay, this);            //создание объекта класса Timer
		time.start();                              //запускает отображение объектов на экране со скоростью delay
	}
	
	public void paint(Graphics g) {
		//определение фона:цвет и границы
		g.setColor(Color.black);
		g.fillRect(1,1, 692, 592);
		
		//мето для отображения элемента
		map.draw((Graphics2D)g); 
		
		//определение границы по периметру о которую может ударяться шар
		g.setColor(Color.yellow);
		g.fillRect(0, 0, 3, 592);  //левая граница
		g.fillRect(0,0 , 692, 3);  //верхняя
		g.fillRect(682,0,3, 592);  //правая граница
		
		//счетчик очков
		g.setColor(Color.white);
		g.setFont(new Font("Verdana", Font.BOLD, 25));
		g.drawString(""+score, 590, 30);

		//платформа
		g.setColor(Color.green);
		g.fillRect(player1, 550, 100,8);  //за х отвечвет игрок тк перемещает платформу вдоль оси
		
		//шар
		g.setColor(Color.yellow);
		g.fillOval(ballposx, ballposy, 20, 20);
		

		if(totalbricks <=0) {    //функция определяющая завершение игры если игрок победил
			play = false;        //статус игры меняется
			ballxdir = 0;        //перемещение шара
			ballydir = 0;
			g.setColor(Color.red);     //ворматируем текс
			g.setFont(new Font("Verdana", Font.BOLD, 35));
			g.drawString("YOU WON!", 190, 300);     
			
			g.setFont(new Font("Verdana", Font.BOLD, 30));
			g.drawString("Press ENTER to restart",230, 350);
		}
		
		if (ballposy > 570) {       //завершение игры если щар вылетел за пределы игрового поля снизу
			play = false;
			ballxdir = 0;
			ballydir = 0;
			g.setColor(Color.red);
			g.setFont(new Font("Verdana", Font.BOLD, 35));
			g.drawString("GAME OVER!", 190, 300);
			
			g.setFont(new Font("Verdana", Font.BOLD, 30));
			g.drawString("Press ENTER to restart",230, 350);
			
		}
		g.dispose();   //заявка на освобождение окна
	}

	@Override //переопределение метода класса ActionEvent(работает с событиями генерирующимся при нажатии кнопок)
	public void actionPerformed(ActionEvent e) {
		time.start();
		if(play) {      //пока идет игра
			//обнаруживание пересечения двух объектов
			if (new Rectangle(ballposx,ballposy, 20, 20).intersects(new Rectangle(player1, 550, 100, 8))) {
				ballydir = -ballydir; //меняем направление по у
			}
			
			B: for (int i=0; i< map.map.length; i++) {      //ставим метку чтобы выйти из цикла
				for (int j=0; j<map.map[0].length; j++) {   //пробегаем по двумерному массиву пространства карты
					if (map.map[i][j]>0) {
						int brickx = j*map.brickwidth + 80;        //высчитываем положение дощечки по х
						int bricky = i* map.brickheight + 50;       //у
						int brickwidth = map.brickwidth;            //размеры дощечки
						int brickheight = map.brickheight;
						
						Rectangle rect = new Rectangle(brickx, bricky, brickwidth, brickheight);    //вносим параметры дощечки
						Rectangle ballrect = new Rectangle(ballposx, ballposy, 20, 20);  //шара
						Rectangle brickrect = rect; 
						
						if(ballrect.intersects(brickrect)) {    //если шар сталкивается с доской
							map.setBrickval(0,i,j);         //дефолтное значение дощечки 1 меняется на 0 что сигналит карте об ее уничтожении
							totalbricks--;                      //их количество уменьшается
							score += 10;                         //увеличивааются очки
							
							if(ballposx + 19 <= brickrect.x || ballposx + 1 >= brickrect.x + brickrect.width) {  //если мы подходим к дощечке слева или справа
								ballxdir = - ballxdir;       //то менем направление по х
							} else {
								ballydir = -ballydir; 
							}
							
							break B;    //выходим из цикла
						}
					}
				}
			}
			ballposx += ballxdir;     //корректируем траекторию шара
			ballposy += ballydir;	  
			if (ballposx < 0) {           //смена направления при передете за предельные границы
				ballxdir = - ballxdir;
			}
			if (ballposy < 0) { 
				ballydir = - ballydir;
			}
			if (ballposx > 670) { 
				ballxdir = - ballxdir;
			}
			
		}
		repaint();      //обновляем отображение объекта
	}

	//определяем неиспользованные методы чтобы избежать ошибок
	@Override
	public void keyTyped(KeyEvent e) {}   
	
	@Override
	public void keyReleased(KeyEvent e) {}


	//определяем поведение клавиатуры
	@Override
	public void keyPressed(KeyEvent e) {               //переопределяем нажатие клавиш
		if(e.getKeyCode() == KeyEvent.VK_RIGHT) {       //если нажата правая стрелка
			if(player1 >= 600) {                          //есом платформа выходит за предельные значения 
				player1 = 600;                            //она за них не выходит
			} else {
				moveright();                              //смещаем вправо
			}
		}
		if(e.getKeyCode() == KeyEvent.VK_LEFT) {         //аналогично для левой стрелки
			if(player1 <10) {
				player1 = 10;
			} else {
				moveleft();
			}
		}
		
		if(e.getKeyCode() == KeyEvent.VK_ENTER) {          //при нажатии enter происходит перезапуск игры и все значения возвращаются к исходным
			if (!play) {
				play = true;
				ballposx = 120;
				ballposy = 350;
				ballxdir = -1;
				ballydir = -2;
				player1 = 310;
				score = 0;
				totalbricks = 21;
				map = new mapbrick(3,7);
				
				repaint();
			};
			
		}
	}

	public void moveright() {       //само смещение относительно окна вправо
		play = true;
		player1+=20;
	}
	public void moveleft() {    //влево
		play = true;
		player1 -=20;
	}
	
}
