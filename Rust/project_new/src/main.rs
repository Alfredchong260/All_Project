use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("猜数");

    let secret_number = rand::thread_rng().gen_range(1, 101);

    loop {

        println!("猜测一个数!");

        // mut 表示可改变的变量
        let mut guess = String::new();

        io:: stdin().read_line(&mut guess).expect("无法读取行");

        // shadow
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue
        };

        println!("你猜测的数是:{}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("数值太小"),
            Ordering::Greater => println!("数值太大"),
            Ordering::Equal => {
                println!("恭喜你猜对了");
                break;
            }
        }
    }
    }

