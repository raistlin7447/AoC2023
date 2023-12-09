use std::fs::read_to_string;

fn main() {
    let file = read_to_string("../python/day01/day01_input.txt");
    let mut total: u32 = 0;
    for line in file.unwrap().lines() {
        let mut numbers: Vec<u32> = Vec::new();
        for char in line.chars() {
            if char.is_digit(10) {
                numbers.push(char.to_digit(10).unwrap());
            }
        }
        let value = numbers.first().unwrap() * 10 + numbers.last().unwrap();
        total += value;
    }
    println!("{:?}", total);
}
