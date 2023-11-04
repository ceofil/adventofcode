use std::fs;
use std::collections::HashSet;

fn test(linie: &str) -> i32{
    let len = linie.len();
    let set1: HashSet<_> = linie.chars().collect();
    let set2: HashSet<_> = linie.chars().collect();
    let common_elements: HashSet<_> = set1.intersection(&set2).cloned().collect();
    println!("{}", common_elements.);
    return linie.len() as i32;
    // return 0;
}

fn main() {
    let contents = fs::read_to_string("input.test").expect("correct input");
    let result :i32 = contents.split("\n").map(
        |line| test(line)
    ).sum();
    println!("{}", result);
}
