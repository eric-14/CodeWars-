I = [12,15]

//find the prime numbers 


int prime_numbers= []
for (i=0,i<=I.length(),i++){

//getting the prime numbers 
for(j=0,j<I[i],j++){

    if (I[i] % j == 0 ){

        factor = I[i] % j 

        for(k=0,k<factor,k++){
            int count_factors = 0
            if (factor % k == 0){
                count_factors++
                if (count_factors <= 1){
                        prime_numbers.add(factor)  
                }else{
                    break;
                } 
            }
        }
    }

}
}




result = []
int sum = 0
for (p=0,p<I.length(),p++){

    sum +=  I[p]

    for(m=0,m<prime_numbers.length(),m++){

        if(sum % prime_numbers[m] == 0 ){
            result.add((prime_numbers[m],sum))
        }
        
        if(I[p] % prime_numbers[m] == 0){
            result.push((I[p],prime_numbers[m]))
        }
    }

}


//sorting my tuples in array according to prime number in ascending

for (i=0, i<result.length(),i++){

    if(result[i][0] > result[i+1][0]){
        int temp = result[i]
        result[i] = result[i+1]
        result[i+1] = temp 
    }
}