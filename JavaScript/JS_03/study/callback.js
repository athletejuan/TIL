function reservation(name, callback){
  console.log(`${name}님`)
  callback()
}

reservation('juan', function(){
  console.log("예약완료")
})
reservation('justin', function(){
  console.log("예약불가")
})