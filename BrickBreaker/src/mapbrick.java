import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics2D;

public class mapbrick {     //класс карты дощечек
	public int map[][];     //которая представляет собой двумерный массив
	public int brickwidth;     
	public int brickheight; 
	public mapbrick (int row, int col) {      //заполнение массива по строкам и столбцам
		map = new int [row][col];              //создаем массив
		for (int i=0; i< map.length; i++) {        
			for (int j=0; j<map[0].length ; j++) {
				map[i][j] = 1;                        //дощечка есть если 1
			}
		}
		
		brickwidth = 540/col;           //ширина ячейки  
		brickheight = 150/row;            //длина
	}
	
	public void draw(Graphics2D g) {             //метод отображения карты
		for (int i=0; i< map.length; i++) {
			for (int j=0; j<map[0].length; j++) {
				if (map[i][j]> 0) {                //если дощнчкаа существует
					g.setColor(Color.white);
					g.fillRect(j*brickwidth + 80,  i*brickheight + 50,  brickwidth,  brickheight);    //раскрашиваем дощечки
					
					//обрисовываем контуры дощечек
					g.setStroke(new BasicStroke(3));   
					g.setColor(Color.black);
					g.drawRect(j*brickwidth +80, i*brickheight + 50, brickwidth, brickheight);
					
				}
			}
		}
	}
	
	//строит актуальную карту дощечек
	public void setBrickval(int val, int row, int col) {
		map[row][col] = val;
	}
}
