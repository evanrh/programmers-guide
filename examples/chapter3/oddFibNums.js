function sumFibs(num) {
   let p = 0;
   let q = 0;
   let current = 1;
   let result = 0;

   while(current <= num) {
      if((current % 2) != 0) {
         result += current;
      }
      p = q;
      q = current;
      current = p + q;
   }
   return result;
}
