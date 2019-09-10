function DNAStrand(dna){
    var array = [];
    for (let value of dna){
      if (value == 'A'){
        array.push('T');
      } else if (value == 'T'){
        array.push('A');
      } else if (value == 'G'){
        array.push('C');
      } else if (value == 'C'){
        array.push('G');
      }
    }
    var string = array.join('');
    return string
  }