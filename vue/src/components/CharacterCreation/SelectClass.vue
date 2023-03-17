<template>
    <div>
        <ContainerBasic>
        <template v-slot:header>Choose a class:</template>
    </ContainerBasic>
    </div>
    
</template>

<script>
import Icon from "../Utility/Icon.vue"
import ContainerBasic from "../Utility/ContainerBasic.vue";
export default {

    name: "SelectClass",

    components: {
        Icon,
        ContainerBasic
    },

}
</script>