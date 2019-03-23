<template>
    <p>{{ greeting }}</p>
</template>

<script>
module.exports = {
    data: function(){
        return {
            greeting: 'Hello World!!!'
        }
    }
}
</script>

<style scoped>
p{
    font-size: 2em;
    text-align: center;
}
</style>

