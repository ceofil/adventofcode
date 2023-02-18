use std::fs;
fn main() {
    let contents: String = fs::read_to_string("input").expect("read file");   
    let mut v: Vec<i32> = contents.split("\n\n").map(
        |s: &str| s.split("\n").map(
            |n: &str| -> i32 {
                n.parse().unwrap()
            }
        ).sum()   
    ).collect();
    v.sort();
    v.reverse();
    let suma: i32 = v[..3].iter().sum();
    println!("{}", suma);
}
