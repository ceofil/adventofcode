use std::fs;
fn main() {
    let contents = fs::read_to_string("input").expect("read file");   
    let mut v: Vec<i32> = contents.split("\n\n").map(
        |s| s.split("\n").map(
            |n: &str| -> i32 {
                n.parse().unwrap()
            }
        ).sum()   
    ).collect();
    v.sort();
    v.reverse();
    let suma: i32 = v[..3].iter().sum();
    println!("{}", suma);
    // let mut v: Vec<i32> = vec![1,2,3];
    // let suma: i32 = v[..2].iter().sum();
    // print!("{suma}")
}
