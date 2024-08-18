<script lang="ts" setup>
import iconPath from 'bootstrap-icons/bootstrap-icons.svg'

defineProps({
    name: {
        type: String,
        required: true
    },
    size: {
        type: Number,
        required: false,
        default: 32
    },
    fill: {
        type: String,
        required: false,
        default: 'currentColor'
    }
})
</script>

<template>
    <svg class="bi" :width="size" :height="size" :fill="fill">
        <use :xlink:href="`${iconPath}#${name}`"/>
    </svg>
</template>
