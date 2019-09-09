<template>
  <div class="text-center">
    <v-btn color="error" @click="overlay = !overlay">
      Show Overlay
    </v-btn>

    <v-overlay :value="overlay">
      <LoginForm />
      <v-btn icon @click="overlay = false">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-overlay>
  </div>
</template>

<script>
import LoginForm from "@/components/login-form.vue";

export default {
  components: {
    LoginForm
  },
  data: () => ({
    overlay: true
  })
};
</script>

<style></style>
