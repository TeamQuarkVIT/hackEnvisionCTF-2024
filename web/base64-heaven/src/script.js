var timeline = new gsap.timeline();
timeline.from("nav",{
    x:1200,
    duration:0.5,
})

timeline.from("nav a",{
    scale:2.5,
    duration:0.3,
    opacity:0,
    x:200,
    y:-200,
    stagger:0.3,
})

gsap.from(".homeImage",{
    scale:2.5,
    borderRadius:"50%",
    opacity:0,
    duration:1,
    
    x:-1200,
    
})

gsap.to(".homeImage",{

    duration:2,
    repeat:-1,
    rotate:360

})