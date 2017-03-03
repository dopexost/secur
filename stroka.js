public class test{
    public static void main(String[] arg) throws IOException{
         Path path = Paths.get("baseShell");
        Charset charset = StandardCharsets.UTF_8;
        String content = new String(Files.readAllBytes(path), charset);
        content = content.substring(content.indexOf("string6"), content.length());
        Files.write(path, content.getBytes(charset));
    }
}